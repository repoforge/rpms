# $Id$
# Authority: shuff
# Upstream: Marcel Gruenauer <marcel$cpan,org>
# ExcludeDist: el3 el4 el5
# Rationale: requires Perl 5.10

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Vim-Tag

Summary: Generate Perl tags for Vim
Name: perl-Vim-Tag
Version: 1.110690
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Vim-Tag/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/Vim-Tag-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.10
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Accessor::Constructor)
BuildRequires: perl(English)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Inherited)
BuildRequires: perl(Hash::Rename)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(constant)
BuildRequires: perl(parent)
BuildRequires: rpm-macros-rpmforge
Requires: bash
Requires: perl >= 5.10
Requires: perl(Class::Accessor::Constructor)
Requires: perl(File::Find)
Requires: perl(File::Slurp)
Requires: perl(Getopt::Inherited)
Requires: perl(Hash::Rename)
Requires: perl(UNIVERSAL::require)
Requires: perl(constant)
Requires: perl(parent)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Manage tags for perl code in vim, with ideas on integrating tags with the bash
programmable completion project.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\\.31.*/ && s/6\\.3\\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# install the Bash profile script
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/profile.d/
%{__install} -m0755 etc/ptags.sh %{buildroot}%{_sysconfdir}/profile.d/

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE META.json README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Vim/Tag.pm
%{perl_vendorlib}/Vim/Tag/*
%{_bindir}/*
%{_sysconfdir}/profile.d/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Apr 25 2011 Steve Huff <shuff@vecna.org> - 1.110960-1
- Initial package.
