# $Id$
# Authority: hadams

Summary: Additional Clearlooks color schemes
Name: gnome-theme-clearlooks-bigpack
Version: 0.6
Release: 6%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://gnomethemes.org/?p=43

Source: http://kwh.kernow-gb.com/~bvc/theme/gtk/clearlooks/Clearlooks-Big_Pack-0.6.x.tar.gz
## Using my own hosting so that the tarball will be versioned; have sent an
## inquiry about this to upstream.
Source1: http://mirror.thecodergeek.com/ALL-CL-Big_Pack-Cairo-%{version}.tar.gz
Patch0: gnome-theme-clearlooks-bigpack-fix-Cairo_Curve-ComboBox-text-contrast.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gtk2-engines >= 2.8

%description
Lots and lots of color schemes for the Clearlooks GTK+ 2.x engine, including
Cairo-enabled schemes for smoother visual rendering.

%prep
%setup -b 0 -c
%setup -D -b 1 -c
%patch0 -p0 

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/themes/
%{__cp} -av Clearlooks* %{buildroot}%{_datadir}/themes/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/themes/*

%changelog
* Sun Jul 08 2007 Heiko Adams <info@fedora-blog.de> - 0.6-6
- Rebuild for RPMforge.

* Tue Apr 10 2007 Peter Gordon <peter@thecodergeek.com> - 0.6-5
- Add patch to fix the longstanding issue of ComboBox hover text having little
  or no contrast when using the Cairo-enabled Curve theme (which also quiets
  some "... not implemented and will be ignored" options).
- Rework %%setup invocations to be more quiet (as they should be).
- Add some text to the %%description to note that we have the Cairo-enabled
  goodness. 

* Sat Nov 04 2006 Peter Gordon <peter@thecodergeek.com> - 0.6-4
- Explicitly depend on gtk2-engines >= 2.8, since we're doing Cairo-enabled
  goodness
- Add bug# to previous %%changelog entry.

* Sat Nov 04 2006 Peter Gordon <peter@thecodergeek.com> - 0.6-3
- Fix homepage URL
- A bunch of aesthetic cleanups to the spec
- Add Cairo-enabled themes (resolves bug #214030)

* Wed Oct 11 2006 Peter Gordon <peter@thecodergeek.com> - 0.6-2
- Bump EVR and rebuild to pick up new dist tag evaluation (for FC6/Devel)
- Use hard tabs instead of spaces for the tags for simplicity

* Fri Dec 23 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> - 0.6-1
- Upstream update

* Thu Apr  7 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> - 0.5-1.fc4
- Dist split

* Wed Apr  6 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> - 0.5-1
- Initial RPM release
