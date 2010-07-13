# $Id$
# Authority: shuff
# Upstream: Mark Grondona <mgrondona$llnl,gov>

Summary: High-performance parallel remote shell utility
Name: pdsh
Version: 2.18
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: https://computing.llnl.gov/linux/pdsh.html

Source: https://downloads.sourceforge.net/project/pdsh/pdsh/pdsh-%{version}/pdsh-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: glibc-devel
# BuildRequires: libgenders-devel
# BuildRequires: libmunge-devel
# BuildRequires: libnodeupdown-devel
# BuildRequires: libslurm-devel
BuildRequires: krb5-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pam-devel
BuildRequires: readline-devel
# BuildRequires: rmsquery
BuildRequires: rpm-macros-rpmforge

Requires: openssh

%description
Pdsh is a high-performance, parallel remote shell utility. It has built-in,
thread-safe clients for Berkeley and Kerberos V4 rsh and can call SSH
externally (though with reduced performance). Pdsh uses a "sliding window"
parallel algorithm to conserve socket resources on the initiating node and to
allow progress to continue while timeouts occur on some connections.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --with-dshgroups \
    --with-exec \
    --with-machines=%{_sysconfdir}/pdsh/machines \
    --with-nodeattr \
    --with-readline \
    --with-ssh \
    --with-xcpu \
    --without-rsh
%{__make} %{?_smp_mflags}

# we are not a devel package
%filter_provides_in %{_libdir}/pdsh
%filter_setup

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/pdsh/
touch %{buildroot}%{_sysconfdir}/pdsh/machines



%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING DISCLAIMER META NEWS README README.KRB4
%doc README.modules README.QsNet TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/pdsh/*.so
%exclude %{_libdir}/pdsh/*.la
%dir %{_sysconfdir}/pdsh/
%config(noreplace) %{_sysconfdir}/pdsh/machines

%changelog
* Tue Jul 13 2010 Steve Huff <shuff@vecna.org> - 2.18-1
- Initial package.
