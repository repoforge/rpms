# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-DecisionTree

Summary: Automatically Learns Decision Trees
Name: perl-AI-DecisionTree
Version: 0.08
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-DecisionTree/

Source: http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/AI-DecisionTree-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The "AI::DecisionTree" module automatically creates so-called "decision
trees" to explain a set of training data. A decision tree is a kind of
categorizer that use a flowchart-like process for categorizing new
instances.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/AI/
%{perl_vendorarch}/AI/DecisionTree/
%{perl_vendorarch}/AI/DecisionTree.pm
%dir %{perl_vendorarch}/auto/AI/
%dir %{perl_vendorarch}/auto/AI/DecisionTree/
%{perl_vendorarch}/auto/AI/DecisionTree/Instance/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
