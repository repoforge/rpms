# $Id$
# Authority: shuff
# Upstream: Lincoln D. Stein <lincoln.stein$gmail,com>
# Rationale: this package totally clobbers a core package, use with care

### EL6 ships with perl-CGI-3.49-115.el6
%{?el6:# Tag: rfx}
### EL3 ships with perl-CGI-2.89-101.EL3
%{?el3:# Tag: rfx}
### EL2 ships with perl-CGI-2.752-37.1.99ent
%{?el2:# Tag: rfx}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI.pm

Summary: Handle Common Gateway Interface requests and responses
Name: perl-CGI
Version: 3.49
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI/

Source: http://search.cpan.org/CPAN/authors/id/L/LD/LDS/CGI.pm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FCGI) >= 0.67
BuildRequires: perl(File::Spec) >= 0.82
#BuildRequires: perl(Test::More) >= 0.80
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.6.0
Requires: perl(FCGI) >= 0.67
Requires: perl(File::Spec) >= 0.82

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description

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
%doc Changes META.yml README cgi-lib_porting.html cgi_docs.html
%doc examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/CGI.pm
%{perl_vendorlib}/CGI/*
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Thu Jul 29 2010 Steve Huff <shuff@vecna.org> - 3.49-1
- Initial package.
