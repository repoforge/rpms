# $Id$
# Authority: shuff
# Upstream: Tim Waugh <twaugh$redhat,com>

Summary: Prevent portmap from binding to specific ports
Name: portreserve
Version: 0.0.5
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://cyberelk.net/tim/software/portreserve/

Source: http://cyberelk.net/tim/data/portreserve/stable/portreserve-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: xmlto
BuildRequires: rpm-macros-rpmforge

%description
The portreserve program aims to help services with well-known ports that lie in
the bindresvport() range. It prevents portmap (or other programs using
bindresvport()) from occupying a real service's port by occupying it itself,
until the real service tells it to release the port (generally in its init
script).

This utility originated in this discussion:

https://bugzilla.redhat.com/show_bug.cgi?id=103401

%prep
%setup

# really?  how did this get through?
%{__perl} -pi -e 's|^DAEMON=.*$|DAEMON=%{_sbindir}/portreserve|;' portreserve.init

%build
%configure \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# install the init script
%{__install} -m755 -d %{buildroot}%{_initrddir}
%{__install} -m755  portreserve.init %{buildroot}%{_initrddir}/portreserve

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post
/sbin/chkconfig --add portreserve || :

%preun
if [ "$1" -eq 0 ]; then
    /sbin/chkconfig --add portreserve || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_initrddir}/*
%{_sbindir}/*

%changelog
* Wed Jul 06 2011 Steve Huff <shuff@vecna.org> - 0.0.5-1
- Initial package.
