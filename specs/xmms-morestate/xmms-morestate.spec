# Authority: dag
# Upstream: David Deephanphongs <deephan@users.sourceforge.net>

%define plugindir %(xmms-config --general-plugin-dir)

Summary: Restores ESD volume, song time, and playing/paused status.
Name: xmms-morestate
Version: 1.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://xmms-morestate.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/xmms-morestate/xmms-morestate-%{version}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

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
%makeinstall bindir="%{buildroot}%{plugindir}"
%{__strip} %{buildroot}%{plugindir}/*.so

### Clean up buildroot
%{__rm} -f %{buildroot}%{plugindir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{plugindir}/*.so
#exclude %{plugindir}/*.la

%changelog
* Wed Jun 25 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
