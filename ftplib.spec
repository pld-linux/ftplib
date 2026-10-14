Summary:	ftplib - set of routines that implement the FTP protocol
Summary(pl.UTF-8):	ftplib - zbiór funkcji implementujących protokół FTP
Name:		ftplib
Version:	4.0.1
Release:	1
License:	Artistic 2.0
Group:		Libraries
Source0:	https://nbpfaus.net/~pfau/ftplib/%{name}-4.0-1.tar.gz
# Source0-md5:	2bb35d21e1647c54032f63f59dfc24e7
Patch0:		%{name}-ldflags.patch
# https://salsa.debian.org/debian/ftplib/-/raw/master/debian/patches/fix-ascii-read-without-eol
Patch1:		%{name}-ascii-readline.patch
Patch2:		%{name}-CVE-2007-1485.patch
Patch3:		%{name}-uint64.patch
Patch4:		%{name}-accept-rv.patch
URL:		https://nbpfaus.net/~pfau/ftplib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ftplib is a set of routines that implement the FTP protocol. They
allow applications to create and access remote files through function
calls instead of needing to fork and exec an interactive ftp client
program.

ftplib has been built and tested on Linux, Mac OS X and OpenVMS.

%description -l pl.UTF-8
ftplib to zbiór funkcji implementujących protokół FTP. Pozwalają one
aplikacjom tworzyć i pobierać zdalne pliki poprzez wywołania funkcji
zamiast wykonywania fork i uruchamiania interaktywnego klienta ftp.

Biblioteka ftplib została zbudowana i przetestowana na Linuksie,
Mac OS X oraz OpenVMS.

%package devel
Summary:	Header files for ftplib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ftplib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ftplib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ftplib.

%package static
Summary:	Static ftplib library
Summary(pl.UTF-8):	Statyczna biblioteka ftplib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ftplib library.

%description static -l pl.UTF-8
Statyczna biblioteka ftplib.

%prep
%setup -q -n %{name}-4.0-1
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%{__make} -C src qftp libftp.so libftp.a \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install src/libftp.so.4.0 $RPM_BUILD_ROOT%{_libdir}
ln -sf libftp.so.4.0 $RPM_BUILD_ROOT%{_libdir}/libftp.so.4
ln -sf libftp.so.4.0 $RPM_BUILD_ROOT%{_libdir}/libftp.so
install src/libftp.a $RPM_BUILD_ROOT%{_libdir}
install src/ftplib.h $RPM_BUILD_ROOT%{_includedir}
install src/qftp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.ftplib-4.0-1 README.qftp additional_rfcs
%attr(755,root,root) %{_bindir}/qftp
%attr(755,root,root) %{_libdir}/libftp.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libftp.so.4

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_libdir}/libftp.so
%{_includedir}/ftplib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libftp.a
