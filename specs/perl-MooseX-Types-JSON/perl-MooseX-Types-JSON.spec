# $Id$
# Upstream: Michael Langner <mila@cpan.org>
# ExcludeDist: el4 


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name MooseX-Types-JSON

Summary: JSON datatype for Moose
Name: perl-MooseX-Types-JSON
Version: 0.02
Release: 2%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Types-JSON

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MILA/MooseX-Types-JSON-%{version}.tar.gz
Patch0: perl-MooseX-Types-JSON-0.02_coercions.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(JSON::XS) >= 2.00
BuildRequires: perl(Moose) >= 0.82
BuildRequires: perl(MooseX::Types) >= 0.15
Requires: perl(JSON::XS) >= 2.00
Requires: perl(Moose) >= 0.82
Requires: perl(MooseX::Types) >= 0.15

%filter_from_requires /^perl*/d
%filter_setup


%description
String type constraints that match valid and relaxed JSON. For the meaning of
'relaxed' see JSON::XS. All the heavy lifting in the background is also done by
JSON::XS.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/MooseX::Types::JSON.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/MooseX/Types/JSON.pm

%changelog
* Tue Sep 27 2011 Steve Huff <shuff@vecna.org> - 0.02-2
- Included type coercions patch (submitted upstream).

* Fri Apr 16 2010 Christoph Maser <cmr.financial.com> - 0.02-1
- initial package
