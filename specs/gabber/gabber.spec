# $Id$
# Authority: matthias

%define real_name Gabber

Summary: Client for the Jabber instant messaging system
Name: gabber
Version: 1.9.4
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gabber.jabberstudio.org/

Source: http://www.jabberstudio.org/files/gabber/Gabber-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gnome-libs-devel, libglade-devel, libsigc++-devel, aspell-devel
BuildRequires: gtkmm2-devel, libgnomemm2-devel, gconfmm2-devel, libglademm2-devel
BuildRequires: gal >= 0.7, gal-devel, openssl-devel

%description
Gabber is a Gnome client for the distributed Open Source instant messaging
system called Jabber. Gabber aims to be a fairly complete client while
remaining easy to use, trying to maintain a balance between too many
features and being powerful enough.

%prep
%setup -n %{real_name}-%{version}


%build
%configure \
        --localstatedir="%{_localstatedir}/lib" \
        --with-release-libs="%{_libdir}" \
        --disable-schemas-install
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
#%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/Gabber/*.{a,la}


%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README* TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/Gabber/
%{_datadir}/pixmaps/Gabber/
%{_datadir}/pixmaps/gabber.png
%{_libdir}/Gabber/


%changelog
* Tue Jun 29 2004 Dag Wieers <dag@wieers.com> - 1.9.4-1
- Updated to release 1.9.4.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.9.3-0
- Updated to release 1.9.3.

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

