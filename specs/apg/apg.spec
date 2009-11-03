# $Id$
# Authority: matthias
# Upstream: Adel I. Mirzazhanov <a-del$iname,com>

Summary: Automated Password Generator for random password generation
Name: apg
Version: 2.2.3
Release: 3%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.adel.nursat.kz/apg/
Source: http://www.adel.nursat.kz/apg/download/apg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
APG (Automated Password Generator) is the tool set for random password
generation. This standalone version generates some random words of
required type and prints them to standard output.


%prep
%setup


%build
# Fix permissions (2.2.3)
%{__chmod} -R u+w .
%{__make} %{?_smp_mflags} standalone


%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 apg %{buildroot}%{_bindir}/apg
%{__install} -Dp -m0644 doc/man/apg.1 %{buildroot}%{_mandir}/man1/apg.1


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README THANKS TODO doc/rfc*
%{_bindir}/apg
%{_mandir}/man?/*


%changelog
* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 2.2.3-3
- Rebuild for Fedora Core 2.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 2.2.3-2
- Rebuild for Fedora Core 1.

* Sat Oct  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.3.

* Sun Aug 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.0.
- Added fix to add +w to the owner of all files from the archive!

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Added _smp_mflags macro.

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.0.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.0final.

* Tue Feb 27 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.13.

* Fri Feb 16 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.11.

* Thu Feb 15 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.1.

* Wed Feb  7 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

