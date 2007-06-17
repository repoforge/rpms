# $Id$
# Authority: dries
# Upstream: Josiah Bryan <jdb$wcoil,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name AI-NeuralNet-BackProp

Summary: Simple back-prop neural net that uses Delta's and Hebbs' rule
Name: perl-AI-NeuralNet-BackProp
Version: 0.77
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AI-NeuralNet-BackProp/

Source: http://search.cpan.org/CPAN/authors/id/J/JB/JBRYAN/AI-NeuralNet-BackProp-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
AI::NeuralNet::BackProp is a simply back-propagation,
feed-foward neural network designed to learn using
a generalization of the Delta rule and a bit of Hopefield
theory.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/AI/NeuralNet/BackProp.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.77-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.77-1
- Initial package.
