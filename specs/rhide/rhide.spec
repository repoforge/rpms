# $Id$
# Authority: dag
# Upstream: Robert Hoehne <robert,hoehne$gmx,net>
# Upstream: <salvador$inti,gov,ar>

Summary: IDE for developing like the old known Borland 3.1 IDE
Name: rhide
Version: 1.5
Release: 1
License: GPL
Group: Development/Debuggers
URL: http://www.rhide.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/rhide/rhide-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires(post): ncurses

%description
RHIDE allows you to develop your programs in an text-based
environment like known from old Borlands`s IDE but improved
and adapted for GNU/Linux. RHIDE supports nearly every compiler,
which gcc supports, and additionally also the pascal compilers
gpc and fpk. The pascal support is somewhat untested but should
work after some runtime configuration on RHIDE.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} \
	RHIDESRC="$(pwd)"

%install
%makeinstall \
	RHIDESRC="$(pwd)"

%post
tic /usr/share/rhide/eterm-rhide

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING* LINUX.TXT README* readme.key RHIDE.BIN rhide.txt VCSA.SH
%doc %{_infodir}/*.inf
%config %{_datadir}/rhide/
%{_bindir}/*

%changelog
* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
