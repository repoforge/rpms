# $Id$

%define desktop_vendor freshrpms

Summary: A GNOME client for the Jabber instant messaging system.
Name: gabber
Version: 0.8.8
Release: fr1
Group: Applications/Communications
License: GPL
URL: http://gabber.sourceforge.net/
Source: http://prdownloads.sourceforge.net/gabber/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
Requires: gnome-libs >= 1.2.0, libglade >= 0.11, libunicode >= 0.4
Requires: libsigc++ >= 1.0.0, gnomemm >= 1.2.0, gal, libxml
BuildRequires: gnome-libs-devel, libglade-devel, libunicode-devel
BuildRequires: libsigc++-devel, gtkmm-devel, gnomemm-devel, gal-devel
BuildRequires: libxml-devel, desktop-file-utils

%description
Gabber is a Gnome client for the distributed Open Source instant messaging 
system called Jabber. Gabber aims to be a fairly complete client while 
remaining easy to use, trying to maintain a balance between too many 
features and being powerful enough.

%prep
%setup -q

%build
%configure --disable-xmms
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}
rm -rf %{buildroot}%{_localstatedir}/scrollkeeper

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category Network                                          \
  %{buildroot}%{_datadir}/gnome/apps/Internet/%{name}.desktop

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING* ChangeLog NEWS README TODO
%{_sysconfdir}/sound/events/%{name}.soundlist
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/gnome/help/%{name}
%{_datadir}/omf/gabber
%{_datadir}/pixmaps/%{name}*
%{_datadir}/sounds/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun May 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.8.

* Thu Jan  2 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Re-enabled SSL by using -DNO_DES as a workaround, thanks to Jima.

* Thu Oct 24 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 8.0.
- Added %%find_lang and the new menu entry.
- Disabled SSL in order to compile :-(
- Update to 0.8.7.12.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Tue Jan  8 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.6.
- Addedd --disable-xmms just in case.

* Mon Jul 23 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.5.

* Mon Jul 23 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.4 and compiled for gnomemm 1.2.0.

* Tue May 15 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for gnomemm 1.1.19.

* Mon May 14 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.3.
- Added forcing of the C*FLAGS, new libgal dependency and %files.

* Wed Apr 25 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file cleanup and rebuilt for Red Hat 7.1.

* Sun Jan 21 2001 Gregory Leblanc <gleblanc@cu-portland.edu>
- some cleanups, trying to make it easier for people to adapt to their
particular distribution.

* Tue Oct 10 2000 Konrad Podloucky <konrad@users.sourceforge.net>
- removed gnet dependency

* Fri May 19 2000  Julian Missig  <julian@linuxpower.org>
- Now using a super generic .spec file. If anyone can tell me why I shouldn't do this, I'll stop.

* Wed May 03 2000  Julian Missig  <julian@linuxpower.org>
- Now using make install-strip to generate a small binary. Much nicer. :)

* Wed Apr 26 2000  Julian Missig  <julian@linuxpower.org>
- Made sure everything seems OK for 0.5.
- Moved to libsigc++ 1.0.0, since older versions are binary incompatible. :(

* Thu Apr 06 2000  Julian Missig  <julian@linuxpower.org>
- Updated to install i18n support

* Sun Apr 02 2000  Julian Missig  <julian@linuxpower.org>
- Updated to install Gabber Manual

* Sat Apr 01 2000  Julian Missig  <julian@linuxpower.org>
- First version of the spec file. It seems to work.

