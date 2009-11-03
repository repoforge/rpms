# $Id$
# Authority: dries
# Upstream: Andrew P. J. Gierth <andrew$erlenstar,demon,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name News-Article

Summary: Object for handling Usenet articles in mail or news form
Name: perl-News-Article
Version: 1.27
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/News-Article/

Source: http://www.cpan.org/modules/by-module/News/News-Article-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module originated with the development of the software intended
to handle newsgroup creation for the (new) mod.* Usenet hierarchy.
The requirement to centralise, and fully automate, the process of
group creation and the detection of defunct groups led to a large
number of cases where the software would be required to read, parse,
forward, reply to, mail and post articles of various forms.

%prep
%setup -n %{real_name}-%{version}

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/News/Article.pm
%{perl_vendorlib}/News/AutoReply.pm
%{perl_vendorlib}/News/FormReply.pm
%{perl_vendorlib}/News/FormArticle.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.27-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Initial package.
