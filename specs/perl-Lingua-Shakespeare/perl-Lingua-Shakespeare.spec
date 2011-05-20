# $Id$
# Authority: shuff
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Shakespeare

Summary: Perl in a Shakespeare play
Name: perl-Lingua-Shakespeare
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Shakespeare/

Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/Lingua-Shakespeare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.4
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.4
Requires: perl(Filter::Util::Call)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Lingua::Shakespeare makes it possible to write Perl programs that are as poetic
as a Shakespeare play.

The language is referred to as SPL (Shakespeare Programming Language)

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc META.yml SIGNATURE
%doc examples/
%doc %{_mandir}/man?/*
%doc %{perl_vendorlib}/Lingua/Shakespeare.pod
%{perl_vendorlib}/Lingua/Shakespeare.pm
%{perl_vendorlib}/Lingua/Shakespeare/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri May 20 2011 Steve Huff <shuff@vecna.org> - 1.00-1
- Initial package.
