# $Id: aget.spec,v 1.4 2004/02/27 17:08:23 driesve Exp $

# Authority: dries

Summary: a console download accelerator
Name: aget
Version: 0.4
Release: 3
License: GPL
Group: Applications/Internet
URL: http://www.enderunix.org/aget/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.enderunix.org/aget/%{name}-%{version}.tar.gz
Patch: errno-include.patch.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}

#(d) primscreenshot: http://www.enderunix.org/aget/aget-shot.jpg

%description
Aget is a multi-threaded download accelerator. It supports HTTP downloads
and can be run from the console.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup
%patch -p 1

%build
%{__make} %{?_smp_mflags}
%{__make} strip

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp -f aget $RPM_BUILD_ROOT/usr/bin/

%files
%defattr(-,root,root, 0755)
%doc AUTHORS COPYING INSTALL README THANKS TODO
%{_bindir}/aget

%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.4-3
- specfile cleanup

* Mon Dec 15 2003 Dries Verachtert <dries@ulyssis.org> 0.4-2
- fixed the Summary (thanks to Koenraad Heijlen)

* Fri Dec 12 2003 Dries Verachtert <dries@ulyssis.org> 0.4-1
- first packaging for Fedora Core 1
