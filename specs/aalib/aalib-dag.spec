# Authority: freshrpms

%define rversion 1.4rc5

Summary: ASCII art library.
Name: aalib
Version: 1.4.0
Release: 0.rc5
Group: System Environment/Libraries
License: LGPL
URL: http://aa-project.sourceforge.net/aalib/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/aa-project/aalib-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: XFree86-devel, ncurses-devel, gpm-devel

%description
AA-lib is a low level graphics library that doesn't require a graphics
device and has no graphics output. Instead AA-lib replaces those
old-fashioned output methods with a powerful ASCII-art renderer. The
AA-Project is working on porting important software like DOOM and Quake
to work with AA-lib.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, gpm-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--with-x \
	--with-curses-driver="yes" \
	--with-ncurses
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall 

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/aalib.info.gz %{_infodir}/dir
/sbin/ldconfig &>/dev/null

%preun
/sbin/install-info --delete %{_infodir}/aalib.info.gz %{_infodir}/dir

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE AUTHORS COPYING ChangeLog NEWS
%doc %{_mandir}/man1/*
%doc %{_infodir}/*
%{_bindir}/aafire
%{_bindir}/aainfo
%{_bindir}/aasavefont
%{_bindir}/aatest
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{_bindir}/aalib-config
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
#exclude %{_libdir}/*.la

%changelog
* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.4rc5-0
- Initial package. (using DAR)
