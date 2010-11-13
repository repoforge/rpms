# $Id$
# Authority: dag

Summary: Small utility for querying NT/2K/XP/2K3/Vista registries
Name: reglookup
Version: 0.9.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://projects.sentinelchicken.org/reglookup/

Source: http://projects.sentinelchicken.org/data/downloads/reglookup-%{version}.tar.gz
Patch0: %{name}-0.9.0-DESTDIR.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
RegLookup is an small command line utility for reading and querying Windows
NT-based registries. RegLookup is released under the GNU GPL, and is
implemented in ANSI C. Original source was borrowed from the program editreg,
written by Richard Sharpe. It has since been rewritten to use the regfio
library, written by Gerald Carter.

Currently the program allows one to read an entire registry and output it in
a (mostly) standardized, quoted format. It also provides features for
filtering of results based on registry path and data type.

%prep
%setup
%patch0 -p1

%build
%{__make} CC="%{__cc}" OPTS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    PREFIX=%{_prefix} \
    MAN_PREFIX="%{_mandir}"

%{__rm} %{buildroot}%{_mandir}/man1/*
%{__mv} %{buildroot}%{_docdir}/reglookup/man/man1/* %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL LICENSE doc/devel/TODO doc/devel/*.txt
%doc %{_mandir}/man1/reglookup.1*
%doc %{_mandir}/man1/reglookup-recover.1*
%doc %{_mandir}/man1/reglookup-timeline.1*
%{_bindir}/reglookup
%{_bindir}/reglookup-recover
%{_bindir}/reglookup-timeline

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Initial package. (using DAR)
