# $Id$

# Authority: dries

Summary: Console download accelerator
Name: aget
Version: 0.4
Release: 4
License: GPL
Group: Applications/Internet
URL: http://www.enderunix.org/aget/
Source: http://www.enderunix.org/aget/%{name}-%{version}.tar.gz
Patch: errno-include.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#(d) primscreenshot: http://www.enderunix.org/aget/aget-shot.jpg

%description
Aget is a multi-threaded download accelerator. It supports HTTP downloads
and can be run from the console.

%prep
%setup
%patch -p1 -b .errno

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__install} -m 0755 -D aget ${RPM_BUILD_ROOT}%{_bindir}/aget

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README THANKS TODO
%{_bindir}/aget

%changelog
* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net> 0.4-4
- More cleanups.
- uncompress the patch (plays better with CVS/SVN).

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.4-3
- specfile cleanup

* Mon Dec 15 2003 Dries Verachtert <dries@ulyssis.org> 0.4-2
- fixed the Summary (thanks to Koenraad Heijlen)

* Fri Dec 12 2003 Dries Verachtert <dries@ulyssis.org> 0.4-1
- first packaging for Fedora Core 1

