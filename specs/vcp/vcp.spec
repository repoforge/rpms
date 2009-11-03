# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

Summary: Enhanced files copying tool
Name: vcp
Version: 1.7.2
Release: 1.2%{?dist}
License: BSD
Group: Applications/File
URL: http://members.optusnet.com.au/~dbbryan/vcp/

Source: http://cudlug.cudenver.edu/gentoo/distfiles/vcp-%{version}.tar.gz
#Source: http://members.optusnet.com.au/~dbbryan/vcp/vcp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ncurses-devel

%description
vcp copies files and directories in a curses interface, with text only
output available. its options and output are similar to BSD's cp while
adding some new features.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0555 vcp %{buildroot}%{_bindir}/vcp
%{__install} -Dp -m0644 vcp.conf.sample %{buildroot}%{_sysconfdir}/vcp.conf
%{__install} -Dp -m0644 vcp.1 %{buildroot}%{_mandir}/man1/vcp.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README vcp.conf.sample
%config(noreplace) %{_sysconfdir}/vcp.conf
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.7.2-1.2
- Rebuild for Fedora Core 5.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Initial package. (using DAR)
