# $Id: _template.spec 765 2004-05-20 17:33:53Z dag $
# Authority: dag
# Upstream: Christopher O'Brien <siege@preoccupied.net>

%define real_name meanwhile-gaim

Summary: Meanwhile Gaim
Name: gaim-meanwhile
Version: 0.78
Release: 1
License: GPL
Group: Applications/Internet
URL: http://meanwhile.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/meanwhile/meanwhile-gaim-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Obsoletes: meanwhile-gaim <= %{version}
Requires: gaim >= 1:0.78, meanwhile >= 0.2

%description
Lotus Sametime Community Client library plugin for Gaim

%prep
%setup -n %{real_name}-%{version}

%build
%configure
# %configure --with-gaim-source=$gaim_src_dir
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -Wall -Werror -I%{_includedir}/gaim/"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/gaim/
%{_datadir}/pixmaps/gaim/

%changelog
* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.78-1
- Initial package. (using DAR)
