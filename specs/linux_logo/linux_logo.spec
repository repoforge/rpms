# $Id$

Summary: The linux logo - a colorful console penguin logo
Name: linux_logo
Version: 4.07
Release: 3.fr
License: GPL
Group: Applications/System
URL: http://www.deater.net/weave/vmwprod/linux_logo/
Source: http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext

%description
Linux logo creates a colorful penguin logo on the console.

%prep
%setup -q

%build
# Disabled many logos since they prevent building on FC1 :-(
#for logo in ./logos/*.logo ./logos/*/*.logo; do
for logo in ./logos/*.logo; do
    echo "$logo" >> logo_config
done
make %{?_smp_mflags} C_OPTS="-I./libsysinfo $RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
make install \
    INSTALL_BINPATH=%{buildroot}%{_bindir} \
    INSTALL_MANPATH=%{buildroot}%{_mandir} \
    INSTALLDIR=%{buildroot}%{_datadir}/locale
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc CHANGES COPYING README LINUX_LOGO.FAQ README* TODO USAGE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 4.07-3.fr
- Disabled many of the logos as they prevent building :-(
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 4.07.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 4.05.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 4.02.
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Thu Feb 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 4.0.
- Included all the existing logos, it's more fun :-)

* Wed Jan  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 3.9b5.
- Added the Red Hat banner (yes, this is an rpm ;-)).

* Thu Apr 26 2001 Matthias Saou <http://freshrpms.net/>
- Update to 3.9b3 and rebuilt for Red Hat 7.1.

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Fri Nov 10 2000 Than Ngo <than@redhat.com>
- update to 3.9b1

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- use RPM macros

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat May 27 2000 Ngo Than <than@redhat.de>
- update to 3.05 for 7.0
- cleanup specfile
- use RPM_OPT_FLAGS

* Thu Nov 18 1999 Ngo Than <than@redhat.de>
- initial RPM
