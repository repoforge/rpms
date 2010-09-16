# $Id: check_logfiles.spec,v 1.1.1.1 2008/10/09 08:54:04 cmr Exp $

Summary: Logfile check  plugin for nagios
Name: check_logfiles
Version: 3.4.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://sourceforge.net/projects/check-logfiles

Source: http://labs.consol.de/wp-content/uploads/2010/06/check_logfiles-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
check_logfiles is a plugin for Nagios which searches for patterns in logfiles. It is capable of scanning multiple logfiles and their rotated ancestors in a single run.


%prep
%setup -n %{name}-%{version}

%build
%configure  --libexecdir=%_libdir/nagios/plugins

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/nagios/plugins/check_logfiles

%changelog
* Thu Sep 16 2010 Christoph Maser <cmaser@gmx.de> - 3.4.2-1
- Update to version 3.4.2.

* Thu Jan 10 2008 Christoph Maser <cmaser@gmx.de> - 2.3.1.2-1
- Initial package.
