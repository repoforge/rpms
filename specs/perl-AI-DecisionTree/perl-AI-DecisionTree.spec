# $Id$
# Authority: dries
# Upstream: Ken Williams <kwilliams$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-DecisionTree

Summary: Automatically Learns Decision Trees
Name: perl-AI-DecisionTree
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-DecisionTree/

Source: http://www.cpan.org/modules/by-module/AI/AI-DecisionTree-%{version}.tar.gz
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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml README eg/
%doc %{_mandir}/man3/AI::DecisionTree.3pm*
%doc %{_mandir}/man3/AI::DecisionTree::*.3pm*
%dir %{perl_vendorarch}/auto/AI/
%{perl_vendorarch}/auto/AI/DecisionTree/
%dir %{perl_vendorarch}/AI/
%{perl_vendorarch}/AI/DecisionTree/
%{perl_vendorarch}/AI/DecisionTree.pm

%changelog
* Mon Oct 06 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
