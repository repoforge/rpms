# $Id$
# Authority: matthias


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Mouse and keyboard sharing utility
Name: synergy
Version: 1.3.1
Release: 2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://synergy2.sourceforge.net/
Source: http://dl.sf.net/synergy2/synergy-%{version}.tar.gz
Patch: synergy-1.2.2-werror.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, autoconf, automake
%{!?_without_modxorg:BuildRequires: libX11-devel, libXt-devel, libXinerama-devel, libXtst-devel, libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its
own display, without special hardware.  It's intended for users
with multiple computers on their desk since each system uses its
own display.

%prep
%setup
%patch -p1 -b .werror

%build
autoreconf
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/PORTING NEWS README
%doc doc/*.css doc/*.html
%doc examples/synergy.conf
%{_bindir}/synergyc
%{_bindir}/synergys

%changelog
* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.3.1-2
- FC6 rebuild.

* Thu May  4 2006 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Update to 1.3.1.
- Run full autoreconf instead of just autoconf since 1.6 is required otherwise.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.2.7-2
- FC5 rebuild.

* Tue Dec 20 2005 Matthias Saou <http://freshrpms.net/> 1.2.7-1
- Update to 1.2.7.
- Add automake build requirement (to get aclocal).
- For %%{fedora} >= 5, buildrequire modular X packages.

* Mon Nov  7 2005 Matthias Saou <http://freshrpms.net/> 1.2.5-1
- Update to 1.2.5, -Werror patch still required.

* Wed Aug 17 2005 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4, -Werror patch still required.

* Wed Aug  3 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Update to 1.2.3, -Werror patch still required (only for warn_unused_result
  anyway).

* Wed May  4 2005 Matthias Saou <http://freshrpms.net/> 1.2.2-3
- Rebuild (my bad with CVS "make tag", I guess).

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.2.2-2
- Disable -Werror as build fails with gcc4 otherwise (temporary fix).

* Mon Jan 31 2005 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2.

* Thu Jan 13 2005 Matthias Saou <http://freshrpms.net/> 1.2.1-1
- Update to 1.2.1.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 1.2.0-1
- Update to 1.2.0.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.14-2
- Rebuilt for Fedora Core 2.

* Wed Jan 21 2004 Matthias Saou <http://freshrpms.net/> 1.0.14-1
- Initial RPM package.

