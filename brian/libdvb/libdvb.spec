Distribution:   CCux
Packager:	Stefan Gottwald <gotti@ccux-linux.de>

Summary:	libdvb package with added CAM library and libdvbmpegtools as well as dvb-mpegtools.
Name:		libdvb
Version:	0.5.5
Release:	2
Provides:	%{name}
License:	GPL
URL:		http://www.metzlerbros.org/dvb
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.gz
Patch0:		libdvb-0.5.5-gentoo.patch 
Patch1:		errno.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	linuxdvb

%description
libdvb package with added CAM library and libdvbmpegtools as well as dvb-mpegtools

%package devel
Summary: 	%{name} development headers.
Group: 		%{group}            
Requires: 	%{name} = %{version}-%{release}

%description devel
Header and include files for developing applications with %{name}.

%prep
%setup -n %{name}-%{version}
%patch0
%patch1
sed -i "s#-I../../include#-I../../include\ -I/lib/modules/`uname -r`/build/include#" config.mk

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT PREFIX=%_prefix install
mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-doc-%{version}/{sample_progs,samplerc}
cp sample_progs/* %{buildroot}/%{_datadir}/doc/%{name}-doc-%{version}/sample_progs/
cp samplerc/* %{buildroot}/%{_datadir}/doc/%{name}-doc-%{version}/samplerc/
cp README %{buildroot}/%{_datadir}/doc/%{name}-doc-%{version}/README
find %{buildroot} -type f \
-exec /usr/bin/strip --strip-debug '{}' ';' 

%files
%defattr(-,root,root)
%{_datadir}/doc/%{name}-doc-%{version}
%_bindir/*

%files devel
%defattr(-,root,root)
%_includedir
%_libdir/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jul 25 2005 Christian Metzen <metzench@ccux-linux.de> 0.5.5-2
- Tweaked specfile, removed doc package
* Sat Jun 18 2005 Stefan Gottwald <gotti@ccux-linux.de> 0.5.5-1
- Initial Release
