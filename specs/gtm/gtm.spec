# $Id$

# Authority: dag

Summary: GNOME Transfer Manager
Name: gtm
Version: 0.4.12
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gtm.sourceforge.net/

Source: http://dl.sf.net/gtm/gtm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: ORBit-devel >= 0.4.0, gnome-libs-devel >= 1.0.59, wget
BuildRequires: oaf-devel
#Requires: wget

%description
GTM allows the user to retrieve multiple files from the web.
These files can be retrieved in multiple parts and each part retrieved on a
separate session that the user is connected to the Internet. This is
most useful to users with dialup connections. The program performs
these tasks using wget as its back-end.

%prep
%setup

%build
%configure \
	--with-gnome \
	--without-debug
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/gtm/
%config %{_sysconfdir}/CORBA/servers/*.gnorba
%config %{_sysconfdir}/sound/events/*.soundlist
%{_bindir}/*
%{_datadir}/applets/Network/*.desktop
%{_datadir}/gnome/apps/Internet/*.desktop
%{_datadir}/idl/*
%{_datadir}/oaf/*
%{_datadir}/pixmaps/*
%{_datadir}/sounds/gtm/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.12-0.2
- Rebuild for Fedora Core 5.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.4.12-0
- Initial package. (using DAR)
