# $Id$
# Authority: shuff
# Upstream: Ziheng Yang <z.yang$ucl,ac,uk>

%define major_release 44

Summary: Phylogenetic Analysis by Maximum Likelihood
Name: paml
Version: 4.4c
Release: 1%{?dist}
License: Freeware
Group: Applications/Engineering
URL: http://abacus.gene.ucl.ac.uk/software/paml.html

Source: http://abacus.gene.ucl.ac.uk/software/paml%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
PAML is a package of programs for phylogenetic analyses of DNA or protein
sequences using maximum likelihood. It is maintained and distributed for
academic use free of charge by Ziheng Yang. ANSI C source codes are distributed
for UNIX/Linux/Mac OSX, and executables are provided for MS Windows. PAML is
not good for tree making. It may be used to estimate parameters and test
hypotheses to study the evolutionary process, when you have reconstructed trees
using other programs such as PAUP*, PHYLIP, MOLPHY, PhyML, RaxML, etc.

%package data
Summary: Data files for PAML
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}

%description data
Data files bundled with PAML.

%prep
%setup -n %{name}%{major_release}

%build
pushd src
%{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 src/baseml %{buildroot}%{_bindir}
%{__install} -m0755 src/basemlg %{buildroot}%{_bindir}
%{__install} -m0755 src/codeml %{buildroot}%{_bindir}
%{__install} -m0755 src/pamp %{buildroot}%{_bindir}
%{__install} -m0755 src/evolver %{buildroot}%{_bindir}
%{__install} -m0755 src/yn00 %{buildroot}%{_bindir}
%{__install} -m0755 src/chi2 %{buildroot}%{_bindir}

%{__install} -d -m0755 %{buildroot}%{_datadir}/paml/dat
%{__install} -m0644 dat/* %{buildroot}%{_datadir}/paml/dat

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt doc/ *.ctl
%{_bindir}/*

%files data
%defattr(-, root, root, 0755)
%doc examples/ Technical/
%{_datadir}/paml

%changelog
* Fri Oct 15 2010 Steve Huff <shuff@vecna.org> - 4.4c-1
- Initial package.
