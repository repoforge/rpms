# $Id: _template.spec 471 2004-05-03 19:42:19Z dag $
# Authority: dag
# Upstream: Lars Lindner <llando@gmx.de>
# Upstream: Nathan J. Conrad <t98502@users.sf.net>

Summary: RSS/RDF feed reader
Name: liferea
Version: 0.5.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://liferea.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/liferea/liferea-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: GConf2-devel >= 2.2, gtkhtml2-devel, libxml2-devel >= 2.5.10
BuildRequires: gettext

%description
Liferea (Linux Feed Reader) is an RSS/RDF feed reader. 
It's intended to be a clone of the Windows-only FeedReader. 
It can be used to maintain a list of subscribed feeds, 
browse through their items, and show their contents 
using GtkHTML.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/liferea.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/liferea/
%{_datadir}/pixmaps/*.png
%{_libdir}/liferea/*.so*
%exclude %{_libdir}/liferea/*.la

%changelog
* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 0.4.9-1
- Updated to release 0.4.9.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.4.8-2
- Added patch for building on RH90 and RHEL3. (Nathan Conrad)

* Fri May 07 2004 Dag Wieers <dag@wieers.com> - 0.4.8-1
- Initial package. (using DAR)
