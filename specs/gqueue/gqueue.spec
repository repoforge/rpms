# $Id$

# Authority: dag

# Upstream: Diego Bazzanella <diegobazzanella@tiscalinet.it>

Summary: A GNOME2 frontend for lpq and lprm working with Cups queues.
Name: gqueue
Version: 0.99.1
Release: 0
License: GPL
Group: Applications/System
URL: http://web.tiscali.it/diegobazzanella/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://web.tiscali.it/diegobazzanella/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: cups-devel

%description
gQueue is a GNOME2 frontend for lpq and lprm working with Cups queues.

You can see all jobs in all printer queues or in the default printer queue,
and delete jobs. It has a GNOME panel applet.

%prep
%setup -n %{name}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/pixmaps/gqueue/

%changelog
* Tue Dec 30 2003 Dag Wieers <dag@wieers.com> - 0.99.1-0
- Updated to release 0.99.1.

* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Fri Mar 21 2003 Dag Wieers <dag@wieers.com> - 0.8-0
- Updated to release 0.8.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Updated to release 0.7.

* Mon Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Updated to release 0.6.

* Fri Jan 31 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
