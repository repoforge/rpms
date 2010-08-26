# $Id$
# Authority: shuff
# Upstream: Anders Nor Berle <debolaz$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Method

Summary: Method declaration with type checking
Name: perl-MooseX-Method
Version: 0.44
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Method/

Source: http://search.cpan.org/CPAN/authors/id/G/GP/GPHAT/MooseX-Method-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP) >= 0.37
# BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Template::Pro) >= 0.65
BuildRequires: perl(Moose) >= 0.22
BuildRequires: perl(Scalar::Util) >= 1.14
BuildRequires: perl(Sub::Name) >= 0.02
BuildRequires: perl(Test::Exception) >= 0.21
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::Pod) >= 1/26
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Class::MOP) >= 0.37
Requires: perl(HTML::Template::Pro) >= 0.65
Requires: perl(Moose) >= 0.22
Requires: perl(Scalar::Util) >= 1.14
Requires: perl(Sub::Name) >= 0.02

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module has been deprecated in favor of MooseX::Method::Signatures. It is
being maintained purely for people who need more time to change their
implementations. It should not be used for new code.

This module is an attempt to solve a problem I've often encountered but never
really found any good solution for: validation of method parameters. How many
times have we all ourselves writing code like this:

  sub foo {
    my ($self,$args) = @_;

    die "Invalid arg1"
      unless (defined $arg->{bar} && $arg->{bar} =~ m/bar/);
  }

Manual parameter validation is a tedious, repetive process and maintaining it
consistently throughout your code can be downright hard sometimes. Modules like
Params::Validate makes the job a bit easier, but it doesn't do much for
elegance and it still requires more weird code than what should, strictly
speaking, be neccesary.

MooseX::Method to the rescue! It lets you declare which parameters people
should pass to your method using Moose-style declaration and Moose types. It
doesn't get much Moosier than this.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml
%doc %{_mandir}/man?/*
%{perl_vendorlib}/MooseX/Method.pm
%{perl_vendorlib}/MooseX/Meta/*
%{perl_vendorlib}/MooseX/Method/*
%{perl_vendorlib}/MooseX/Test/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Aug 26 2010 Steve Huff <shuff@vecna.org> - 0.44-1
- Initial package.
