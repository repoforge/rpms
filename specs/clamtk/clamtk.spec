# $Id$
# Authority: dag
# Upstream: Dave M <dave-m$jabber,org>

### FIXME: do something with clamtk.xml (shared-mime-info)

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Easy to use front-end for ClamAV
Name: clamtk
Version: 4.25
Release: 1%{?dist}
License: Perl
Group: Applications/File
URL: http://clamtk.sourceforge.net/

Source: http://downloads.sourceforge.net/project/clamtk/ClamTk/%{version}/clamtk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: perl(Date::Calc)
Requires: perl(File::Find::Rule)
Requires: perl(Gtk2)
Requires: perl(LWP)
Requires: clamav >= 0.90, clamav-db

Provides: perl(ClamTk::App) = %{version}
Provides: perl(ClamTk::GUI) = %{version}
Provides: perl(ClamTk::Prefs) = %{version}
Provides: perl(ClamTk::Results) = %{version}
Provides: perl(ClamTk::Schedule) = %{version}
Provides: perl(ClamTk::Update) = %{version}

Obsoletes: clamtk2

%description
ClamTk is a front-end, point and click gui for ClamAV on Linux systems.
It supports easy signature-updates.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 clamtk %{buildroot}%{_bindir}/clamtk
%{__install} -Dp -m0644 clamtk.1.gz %{buildroot}%{_mandir}/man1/clamtk.1
%{__install} -Dp -m0644 clamtk.xpm %{buildroot}%{_datadir}/pixmaps/clamtk.xpm
%{__install} -Dp -m0644 clamtk.png %{buildroot}%{_datadir}/pixmaps/clamtk.png

# Perl modules
%{__install} -d -m0755 %{buildroot}%{perl_vendorlib}/ClamTk
%{__install} -Dp -m0644 lib/App.pm %{buildroot}%{perl_vendorlib}/ClamTk/
%{__install} -Dp -m0644 lib/GUI.pm %{buildroot}%{perl_vendorlib}/ClamTk/
%{__install} -Dp -m0644 lib/Prefs.pm %{buildroot}%{perl_vendorlib}/ClamTk/
%{__install} -Dp -m0644 lib/Results.pm %{buildroot}%{perl_vendorlib}/ClamTk/
%{__install} -Dp -m0644 lib/Schedule.pm %{buildroot}%{perl_vendorlib}/ClamTk/
%{__install} -Dp -m0644 lib/Update.pm %{buildroot}%{perl_vendorlib}/ClamTk/

%if %{?_without_freedesktop:1}0
    %{__install} -Dp -m0644 clamtk.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/clamtk.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --delete-original \
        --vendor %{desktop_vendor}                 \
        --dir %{buildroot}%{_datadir}/applications \
        --add-category X-Red-Hat-Base              \
        clamtk.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES DISCLAIMER LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/clamtk
%{perl_vendorlib}/ClamTk
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-clamtk.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/clamtk.desktop}
%{_datadir}/pixmaps/clamtk.xpm
%{_datadir}/pixmaps/clamtk.png

%changelog
* Thu Apr 22 2010 Steve Huff <shuff@vecna.org> - 4.25-1
- Updated to release 4.25.
- Changed source location.
- Rewrote Perl dependencies.

* Tue May 27 2008 Dag Wieers <dag@wieers.com> - 3.09-1
- Updated to release 3.09.

* Thu Feb 07 2008 Dag Wieers <dag@wieers.com> - 3.08-1
- Updated to release 3.08.

* Sun May 13 2007 Dag Wieers <dag@wieers.com> - 2.32-1
- Updated to release 2.32.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 2.30-1
- Updated to release 2.30.

* Fri Feb 23 2007 Dag Wieers <dag@wieers.com> - 2.28-1
- Updated to release 2.28.

* Sun Jan 14 2007 Dries Verachtert <dries@ulyssis.org> - 2.27-1
- Updated to release 2.27.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.26-1
- Updated to release 2.26.

* Wed May 17 2006 Dag Wieers <dag@wieers.com> - 2.19-1
- Updated to release 2.19.

* Mon May 08 2006 Dag Wieers <dag@wieers.com> - 2.14-1
- Updated to release 2.14.

* Sun Jan 01 2006 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release 2.13.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release 2.10.

* Sun Aug 21 2005 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Thu May 19 2005 Dag Wieers <dag@wieers.com> - 1.99-1
- Updated to release 1.99.

* Thu May 05 2005 Dag Wieers <dag@wieers.com> - 1.97-1
- Updated to release 1.97.
- Added changes from Dave M.

* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 1.0.10-1
- Initial package. (using DAR)
