# $Id$
# Authority: dag

Summary: GNOME IRDA applet
Name: girda_applet
Version: 2.0.3
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://girda.sourceforge.net/

Source: http://dl.sf.net/girda/girda_applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel, gtk+-devel >= 1.2.9, gnome-libs-devel >= 1.2.11, ORBit-devel >= 0.5.7
BuildRequires: gdk-pixbuf-devel >= 0.11, libglade2-devel
#BuildRequires: openobex-devel
BuildRequires: scrollkeeper, gtk2-devel, libwnck-devel
BuildRequires: gnome-panel-devel, gettext

Requires(post): scrollkeeper

%description
GNOME IrDA Monitor is a GNOME applet. The applet is monitoring the
ir port, and lists ir devices in range.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--with-gnome \
	--without-debug \
	--enable-openobex
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang girda-2.0

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f girda-2.0.lang
%defattr(-, root, root, 755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/girda_applet/
%{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/girda_applet/
%{_datadir}/omf/girda_applet/
%{_datadir}/pixmaps/girda_applet/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.3-1.2
- Rebuild for Fedora Core 5.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 2.0.3-0
- Initial package. (using DAR)
