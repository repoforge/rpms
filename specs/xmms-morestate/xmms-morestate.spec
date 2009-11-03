# $Id$
# Authority: dag
# Upstream: David Deephanphongs <deephan$users,sourceforge,net>

%define xmms_generaldir %(xmms-config --general-plugin-dir)

Summary: Restores ESD volume, song time, and playing/paused status
Name: xmms-morestate
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://xmms-morestate.sourceforge.net/

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
* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-0.2
- Rebuild for Fedora Core 5.

* Wed Jun 25 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
