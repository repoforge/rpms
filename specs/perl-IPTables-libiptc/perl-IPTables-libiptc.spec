# $Id$
# Authority: shuff
# Upstream: Jesper Dangaard Brouer <hawk$comx,dk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPTables-libiptc

Summary: Perl extension for iptables libiptc
Name: perl-IPTables-libiptc
Version: 0.51
Release: 2%{?dist}
License: GPLv2+
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPTables-libiptc/

Source: http://search.cpan.org/CPAN/authors/id/H/HA/HAWK/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: iptables-devel >= 1.4
BuildRequires: rpm-macros-rpmforge

BuildRequires: perl
BuildRequires: perl(AutoLoader)
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

Requires: perl(AutoLoader)
Requires: perl(Carp)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This package provides a perl interface to the netfilter/iptables
C-code and library C<libiptc>.

Advantages of this module: Many rule changes can be done very
fast. Several rule changes is committed atomically.

This module is heavily inspired by the CPAN module IPTables-IPv4.  The
CPAN module IPTables-IPv4 could not be used because it has not been
kept up-to-date, with the newest iptables extensions.  This is a
result of the module design, as it contains every extension and thus
needs to port them individually.

This package has another approach, it links with the systems libiptc.a
library and depend on dynamic loading of iptables extensions available
on the system.

The module only exports the libiptc chain manipulation functions.  All
rule manipulations are done through the iptables.c C<do_command>
function.  As iptables.c is not made as a library, the package
unfortunately needs to maintain/contain this C file.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/IPTables/
%{perl_vendorarch}/IPTables/*
%{perl_vendorarch}/auto/IPTables/libiptc/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Sep 9 2011 Olivier Bilodeau <obilodeau@inverse.ca> - 0.51-2
- Initial package.
