# $Id$
# Authority: dries
# Upstream: <kitone$free,fr>

Summary: Subtitle editor
Name: subtitleeditor
Version: 0.12.4
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://kitone.free.fr/subtitleeditor/

Source: http://kitone.free.fr/subtitleeditor/files/subtitleeditor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gstreamer-plugins-base-devel, gtk2-devel, gtkmm24-devel, libglademm24-devel
BuildRequires: gstreamer-devel, pcre-devel, gettext

%description
Subtitle Editor is a tool to create subtitles or to transform, edit, correct 
and refine existing subtitle.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/subtitleeditor*
%{_bindir}/subtitleeditor
%{_datadir}/subtitleeditor/
%{_datadir}/applications/subtitleeditor.desktop

%changelog
* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.12.4-1
- Initial package.
