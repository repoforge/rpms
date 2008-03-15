# $Id$
# Authority: 	dag
%define         name    	rspam
%define         version 	0.0.6
%define         release 	1
%define         prefix  	/usr
%define		gtk2		2.10.4
%define		libgnome	2.7.0
%define		libgnomeui	2.7.0
%define		evreq		2.8.0
%define		razor		2.84

Summary:	Rspam Evolution Plugin
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License:        GPL
Group:          Applications/Internet
Source: 	http://mips.edu.ms/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: 		http://mips.edu.ms/
Requires:	gtk2 >= %gtk2
Requires:	libgnomeui >= %libgnomeui
Requires:	evolution >= %evreq
Requires:	razor-agents >= %razor
BuildRequires:  evolution-devel, evolution-data-server-devel

%description
Rspam Evolution Plugin enables Evolution Mail client to report email messages
as spam to checksum-based and statistical filtering networks.
It supports Razor network, DCC, and SpamCop.
This plugins requires a pretty new version of evolution to build.
See README for more information about required programs.

%prep
%setup -q -n rspam-%{version}
%{__perl} -pi.orig -e 's|evolution-plugin-2.6|%{evolution_basename}|g' configure

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_datadir}/evolution/2.8/images/spam.gif
%{_datadir}/evolution/2.8/images/nspam.gif
%{_datadir}/evolution/2.8/errors/org-gnome-sa-rspam.error
%{_libdir}/evolution/2.8/plugins/org-gnome-sa-rspam.eplug
%{_libdir}/evolution/2.8/plugins/liborg-gnome-sa-rspam.so
%{_libdir}/evolution/2.8/plugins/liborg-gnome-sa-rspam.la
/etc/gconf/schemas/rspam.schemas
%{_datadir}/locale/en_AU/LC_MESSAGES/rspam.mo
%{_datadir}/locale/ro_RO/LC_MESSAGES/rspam.mo
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc INSTALL
%doc NEWS
%doc README
%doc TODO

%changelog
* Sat Mar 16 2008 Heiko Adams <info-2007{at}fedora-blog.de> - 0.0.6-1
- update to version 0.0.6

* Sat Jun 16 2007 Heiko Adams <info@fedora-blog.de>
- Initial package for rpmForge.
