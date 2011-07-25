# $Id$
# Authority: dag
# Upstream: Nagios Plugin Development Team <nagiosplug-devel$lists,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Nagios-Plugin

Summary: Family of perl modules to streamline writing Nagios
Name: perl-Nagios-Plugin
Version: 0.35
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Nagios-Plugin/

Source: http://www.cpan.org/modules/by-module/Nagios/Nagios-Plugin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Config::Tiny)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(Math::Calc::Units)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More) >= 0.62
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Class::Accessor)
Requires: perl(Class::Accessor::Fast)
Requires: perl(Config::Tiny)
Requires: perl(File::Basename)
Requires: perl(File::Spec)
Requires: perl(IO::File)
Requires: perl(Math::Calc::Units)
Requires: perl(Params::Validate)

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Nagios::Plugin and its associated Nagios::Plugin::* modules are a family of
perl modules to streamline writing Nagios plugins. The main end user modules
are Nagios::Plugin, providing an object-oriented interface to the entire
Nagios::Plugin::* collection, and Nagios::Plugin::Functions, providing a
simpler functional interface to a useful subset of the available functionality.

The purpose of the collection is to make it as simple as possible for
developers to create plugins that conform the Nagios Plugin guidelines
(http://nagiosplug.sourceforge.net/developer-guidelines.html).

%prep
%setup -n %{real_name}-%{version}

# fix the busted shebangs
%{__perl} -pi -e 's|^#!/usr/local/bin/perl|#!%{_bindir}/perl|;' t/check_stuff.*

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README t/check_stuff.pl
%doc %{_mandir}/man3/Nagios::Plugin.3pm*
%doc %{_mandir}/man3/Nagios::Plugin::*.3pm*
%dir %{perl_vendorlib}/Nagios/
%{perl_vendorlib}/Nagios/Plugin/
%{perl_vendorlib}/Nagios/Plugin.pm

%changelog
* Mon Jul 25 2011 Steve Huff <shuff@vecna.org> - 0.35-2
- Filter out bogus /usr/local/bin/perl dep from example script.

* Tue Jul 05 2011 Steve Huff <shuff@vecna.org> - 0.35-1
- Updated to version 0.35.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.33-1
- Updated to version 0.33.

* Mon Dec 22 2008 Christoph Maser <cmr@financial.com> - 0.31-1
- Updated to release 0.31

* Mon Dec 22 2008 Christoph Maser <cmr@financial.com> - 0.30-2
- Added dependency for perl(Class::Accessor::Fast)

* Mon Dec 15 2008 Christoph Maser <cmr@financial.com> - 0.30-1
- Updated to release 0.30.

* Tue Jul 01 2008 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Sat Mar 15 2008 Dag Wieers <dag@wieers.com> - 0.24-2
- Added perl(Config::Tiny) as a dependency.

* Thu Mar 13 2008 Dag Wieers <dag@wieers.com> - 0.24-1
- Initial package. (using DAR)
