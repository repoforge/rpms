# $Id$
# Authority: hadams

%define		_evolution_version	 2.8

Name:		evolution-rss
Version:	0.0.4
Release:	1
Summary:	This is an evolution plugin which enables evolution to read rss feeds.
URL:		http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin
Group:		Productivity/Networking/Email/Clients
License:	GPL
Source0:	http://mips.edu.ms/%{name}-%{version}.tar.gz
Requires:	evolution
BuildRequires:	evolution-devel
BuildRequires:	gettext-devel
BuildRequires:	perl-XML-Parser
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is an evolution plugin which enables evolution to read rss feeds.

%prep
%setup -q 

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.lang 
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_datadir}/evolution/%{_evolution_version}/errors/*
%{_datadir}/evolution/%{_evolution_version}/images/*
%{_libdir}/evolution/%{_evolution_version}/plugins/*
%{_libdir}/bonobo/servers/*
/glade/*

%changelog
* Mon Jul 03 2007 Heiko Adams <info@fedora-blog.de> - 0.0.4-1
- update to 0.0.4

* Sat Jun 30 2007 Heiko Adams <info@fedora-blog.de> - 0.0.3-2
- Rebuild for CentOS

* Sun May 20 2007 Piotr Pacholak <obi.gts@gmail.com>
- Initial release
