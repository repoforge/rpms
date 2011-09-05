# $Id$
# Authority:    hadams

%define nodoka_dir %{_datadir}/themes/Nodoka

Name:           nodoka-theme-gnome
Version:        0.3.2
Release:        4%{?dist}
Summary:        The Nodoka Theme Pack for Gnome

Group:          System Environment/Libraries
License:        GPLv2
URL:            http://hosted.fedoraproject.org/projects/nodoka

# can get on a wiki, see URL
Source0:        %{name}-%{version}.tar.gz 

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

#Requires:       gtk2-engines-nodoka >= 0.3.1.1
Requires:       gtk-nodoka-engine >= 0.6.2
Requires:       nodoka-metacity-theme
#Requires:       fedora-icon-theme

%description
The Nodoka Theme Pack for Gnome make use of Nodoka Metacity theme, Nodoka gtk2
theme and Echo Icon set.


# subpackage has inverse relationship to the main package
# the reason is that metacity theme is a part of the whole theme and as its
# in one source with the metatheme the nodoka-theme-gnome seems more rational
# to be the name of the main package

%package -n     nodoka-metacity-theme
Summary:        The Nodoka theme for Metacity 
Group:          System Environment/Libraries
Requires:       metacity

# needed for dir ownership
Requires:       gtk2-engines-nodoka

%description -n nodoka-metacity-theme
The Nodoka theme for metacity. A clean theme featuring soft gradients and 
Echoey look and feel.

%prep
%setup -q -n nodoka-theme-gnome


%build

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -Dp -m 0644 Nodoka/index.theme                             $RPM_BUILD_ROOT/%{nodoka_dir}/index.theme
%{__install} -Dp -m 0644 Nodoka/metacity-1/button_close.png             $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/button_close.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/button_maximize.png          $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/button_maximize.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/button_minimize.png          $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/button_minimize.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/menu_button_close.png        $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/menu_button_close.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/menu_button_maximize.png     $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/menu_button_maximize.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/menu_button_minimize.png     $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/menu_button_minimize.png
%{__install} -Dp -m 0644 Nodoka/metacity-1/metacity-theme-1.xml         $RPM_BUILD_ROOT/%{nodoka_dir}/metacity-1/metacity-theme-1.xml

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{nodoka_dir}/index.theme

%files -n nodoka-metacity-theme
%defattr(-,root,root,-)
%{nodoka_dir}/metacity-1


%changelog
* Sun Feb 17 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.3.2-4
- Updated for latest nodoka release

* Sun Dec 16 2007 Heiko Adams <info-2007@fedora-blog.de> - 0.3.2-3
- rebuild for rpmforge

* Thu Sep 27 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.2-2
- Require fedora-icon-theme instead of redhat-artwork (rhbz #309631)

* Thu Sep 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.2-1.fc8.1
- fix dir name

* Thu Sep 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.2-1
- new version, reworked gradients in metacity theme

* Sat Aug 11 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.2-1
- new version, change used icon set to fedora (in redhat-artwork pkg)

* Thu Aug 09 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-4
- update License: field to GPLv2

* Sat Aug 04 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-3
- fix dir ownership
- add a comment about the inverse relationship of the main package to the 
  subpackage
- add a comment about upstream sources location

* Fri Jul 27 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-2
- remove empty %%dir for nodoka-metacity-theme
- fix the %%description to be more sane

* Fri Jul 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 0.3.1.1-1
- split metacity and metatheme into separate package in upstream
