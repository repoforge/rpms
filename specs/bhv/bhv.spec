# $Id$
# Authority: dries
# Upstream: Loren Bandiera <lorenb$mmgsecurity,com>

Summary: Examine the contents of a web browser history
Name: bhv
Version: 0.0.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://people.mmgsecurity.com/~lorenb/bhv/

Source: http://people.mmgsecurity.com/~lorenb/bhv/releases/bhv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, python, intltool, perl-XML-Parser
BuildRequires: pygtk2-devel, gnome-python2, pygtk2-libglade, scrollkeeper

%description
browser-history-viewer allows you to examine the contents of Web browser
history. It is meant to be a forensics tool.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/browser-history-viewer*
%{_bindir}/browser-history-viewer
%{_libdir}/bhv/
%{_datadir}/application-registry/bhv.applications
%{_datadir}/applications/bhv.desktop
%{_datadir}/gnome/help/bhv/
%{_datadir}/omf/bhv/
%exclude %{_var}/scrollkeeper

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.2-1.2
- Rebuild for Fedora Core 5.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.2-1
- Initial package.
