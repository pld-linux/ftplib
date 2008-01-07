Summary:	ftplib - set of routines that implement the FTP protocol
Summary(pl.UTF-8):	ftplib - zbiór funkcji implementujących protokół FTP
Name:		ftplib
Version:	3.1.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://nbpfaus.net/~pfau/ftplib/%{name}-3.1-1.tar.gz
# Source0-md5:	763be9c7e7b110776f88521a558dbc55
URL:		http://nbpfaus.net/~pfau/ftplib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ftplib is a set of routines that implement the FTP protocol. They
allow applications to create and access remote files through function
calls instead of needing to fork and exec an interactive ftp client
program.

ftplib has been built and tested on Linux, VMS, OSF/1 and Windows NT.

%description -l pl.UTF-8
ftplib to zbiór funkcji implementujących protokół FTP. Pozwalają one
aplikacjom tworzyć i pobierać zdalne pliki poprzez wywołania funkcji
zamiast wykonywania fork i uruchamiania interaktywnego klienta ftp.

Biblioteka ftplib została zbudowana i przetestowana na Linuksie,
VMS-ie, OSF/1 oraz Windows NT.

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
%setup -q -n %{name}-3.1-1

%build
%{__make} -C src \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install src/libftp.so.3.1 $RPM_BUILD_ROOT%{_libdir}
ln -sf libftp.so.3.1 $RPM_BUILD_ROOT%{_libdir}/libftp.so.3
ln -sf libftp.so.3.1 $RPM_BUILD_ROOT%{_libdir}/libftp.so
install src/libftp.a $RPM_BUILD_ROOT%{_libdir}
install src/ftplib.h $RPM_BUILD_ROOT%{_includedir}
install src/qftp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES NOTES README.ftplib_v3.1 README.qftp TODO additional_rfcs
%attr(755,root,root) %{_bindir}/qftp
%attr(755,root,root) %{_libdir}/libftp.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libftp.so.3

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_libdir}/libftp.so
%{_includedir}/ftplib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libftp.a
