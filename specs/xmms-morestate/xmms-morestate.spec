# $Id$
# Authority: dag
# Upstream: David Deephanphongs <deephan$users,sourceforge,net>

%define xmms_generaldir %(xmms-config --general-plugin-dir)

Summary: Restores ESD volume, song time, and playing/paused status
Name: xmms-morestate
Version: 1.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://xmms-morestate.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/xmms-morestate/xmms-morestate-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel


%description
XMMS Morestate restores ESD volume, song time, and playing/paused status.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	bindir="%{buildroot}%{xmms_generaldir}"
%{__strip} %{buildroot}%{xmms_generaldir}/*.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{xmms_generaldir}/*.so
#%exclude %{xmms_generaldir}/*.la


%changelog
* Wed Jun 25 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
