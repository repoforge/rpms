# $Id$
# Authority: dag

Summary: Library and tools for handling papersize
Name: libpaper
Version: 1.1.22
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://packages.qa.debian.org/libp/libpaper.html

Source: http://ftp.debian.org/debian/pool/main/libp/libpaper/libpaper_%{version}.tar.gz
Patch0: libpaper-1.1.20-automake_1.10.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtool, gettext, gawk

%description
The paper library and accompanying files are intended to provide a 
simple way for applications to take actions based on a system- or 
user-specified paper size. This release is quite minimal, its purpose 
being to provide really basic functions (obtaining the system paper name 
and getting the height and width of a given kind of paper) that 
applications can immediately integrate.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1
%{__cp} -v debian/NEWS NEWS

%{__cat} <<EOF >papersize.conf
# Simply write the paper name. See papersize(5) for possible values
EOF

%build
touch AUTHORS
autoreconf --force --install --symlink
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/libpaper.d/
%{__install} -Dp -m0644 papersize.conf %{buildroot}%{_sysconfdir}/papersize

for file in debian/po/*.po; do
    lang="$(basename $file .po)"
    %{__install} -d -m0755 %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
    msgfmt $file -o %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/libpaper.mo;
done
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/paperconf.1*
%doc %{_mandir}/man5/papersize.5*
%doc %{_mandir}/man8/paperconfig.8*
%config(noreplace) %{_sysconfdir}/papersize
%dir %{_sysconfdir}/libpaper.d/
%{_bindir}/paperconf
%{_libdir}/libpaper.so.*
%{_sbindir}/paperconfig

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3*
%{_includedir}/paper.h
%{_libdir}/libpaper.so
%exclude %{_libdir}/libpaper.la

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.1.22-1
- Initial package. (using DAR)
