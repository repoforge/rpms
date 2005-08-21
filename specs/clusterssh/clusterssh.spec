# $Id$
# Authority: duncan
# Upstream: Duncan Ferguson <duncan_ferguson$users,sf,net>

%define perl_version %(eval "$(%{__perl} -V:version)"; echo $version)

Summary: Secure concurrent multi-server terminal control
Name: clusterssh
Version: 3.17.1
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://clusterssh.sourceforge.net/

Source: http://download.sourceforge.net/clusterssh/clusterssh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl => 1:5.6.1, perl(Tk), perl(X11::Protocol)
Requires: perl(:MODULE_COMPAT_%{perl_version})

%description
Control multiple terminals open on different servers to perform administration
tasks.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/cssh.1*
%{_bindir}/cssh

%changelog
* Thu Aug 18 2005 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.17.1-1
- Initial version.
