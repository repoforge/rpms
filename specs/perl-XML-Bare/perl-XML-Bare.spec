# $Id$
# Authority: shuff
# Upstream: David Helkowski <cpan$codechild,com>
# ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Bare

Summary: A minimal XML parser using C internally.
Name: perl-XML-Bare
Version: 0.45
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Bare/

Source: http://search.cpan.org/CPAN/authors/id/C/CO/CODECHILD/XML-Bare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildArch: noarch
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: perl >= 5.006
BuildRequires: perl(Carp)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.006
Requires: perl(Carp)
Requires: perl(DynaLoader)
Requires: perl(Exporter)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module is a 'Bare' XML parser. It is implemented in C. The parser itself
is a simple state engine that is less than 500 lines of C. The parser builds a
C struct tree from input text. That C struct tree is converted to a Perl hash
by a Perl function that makes basic calls back to the C to go through the nodes
sequentially.

The parser itself will only cease parsing if it encounters tags that are not
closed properly. All other inputs will parse, even invalid inputs. To allowing
checking for validity, a schema checker is included in the module as well.

The schema format is custom and is meant to be as simple as possible. It is
based loosely around the way multiplicity is handled in Perl regular
expressions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/XML/Bare.pm
%{perl_vendorarch}/auto/*
#%{perl_vendorlib}/XML/Bare/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jan 26 2011 Steve Huff <shuff@vecna.org> - 0.45-1
- Initial package.
