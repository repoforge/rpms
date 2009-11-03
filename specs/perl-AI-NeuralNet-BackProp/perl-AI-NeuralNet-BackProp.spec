# $Id$
# Authority: dries
# Upstream: Josiah Bryan <jdb$wcoil,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-NeuralNet-BackProp

Summary: Simple back-prop neural net that uses Delta's and Hebbs' rule
Name: perl-AI-NeuralNet-BackProp
Version: 0.89
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-NeuralNet-BackProp/

Source: http://search.cpan.org/CPAN/authors/id/J/JB/JBRYAN/AI-NeuralNet-BackProp-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
AI::NeuralNet::BackProp is a simply back-propagation,
feed-foward neural network designed to learn using
a generalization of the Delta rule and a bit of Hopefield
theory.

%prep
%setup -c %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes docs.htm MANIFEST README examples/
%doc %{_mandir}/man3/AI::NeuralNet::BackProp.3pm*
%{perl_vendorlib}/AI/NeuralNet/BackProp.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.89-1
- Updated to release 0.89.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.77-1
- Initial package.
