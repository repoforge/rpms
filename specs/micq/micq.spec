# $Id$
# Authority: dag
# Upstream: RÃdiger Kuhlmann <info$ruediger-kuhlmann,de>
# Upstream: <micq-list$micq,org>

%{?dist: %{expand: %%define %dist 1}}

Summary: Clone of the Mirabilis ICQ online messaging program
Name: micq
Version: 0.4.11
Release: 1
Group: Applications/Internet
License: GPL
URL: http://www.micq.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.micq.org/source/micq-%{version}.tgz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, tcl
%{!?dist:BuildRequires: libgcrypt-devel, gnutls-devel, tcl-devel}
%{?el4:BuildRequires: libgcrypt-devel, gnutls-devel, tcl-devel}
%{?fc3:BuildRequires: libgcrypt-devel, gnutls-devel, tcl-devel}
%{?fc2:BuildRequires: libgcrypt-devel, gnutls-devel, tcl-devel}
%{?fc1:BuildRequires: libgcrypt-devel, gnutls-devel, tcl-devel}
#%{?el3:BuildRequires: libgcrypt-devel, gnutls-devel, tcl-devel}
%{?el3:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?rh9:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?rh8:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?rh7:BuildRequires: libgcrypt-devel}

%description
Micq is a clone of the Mirabilis ICQ online messaging/conferencing
program.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* FAQ NEWS README TODO doc/README* doc/*.txt
%doc %{_mandir}/man?/micq*
%{_bindir}/micq
%{_datadir}/micq/

%changelog
* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 0.4.11-1
- Initial package. (using DAR)
