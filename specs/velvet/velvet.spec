# $Id$
# Authority: shuff
# Upstream: Daniel Zerbino <zerbino$ebi,ac,uk>

Summary: Sequence assembler for very short reads
Name: velvet
Version: 1.0.13
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://www.ebi.ac.uk/~zerbino/velvet/ 

Source: http://www.ebi.ac.uk/~zerbino/velvet/velvet_%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}
%filter_setup

%description
Velvet is a de novo genomic assembler specially designed for short read
sequencing technologies, such as Solexa or 454, developed by Daniel Zerbino and
Ewan Birney at the European Bioinformatics Institute (EMBL-EBI), near
Cambridge, in the United Kingdom.

Velvet currently takes in short read sequences, removes errors then produces
high quality unique contigs. It then uses paired-end read and long read
information, when available, to retrieve the repeated areas between contigs. 

This package takes the following arguments at rpmbuild:

    --define 'categories <INTEGER>'    
        set the CATEGORIES parameter (default 2)

    --define 'maxkmerlength <INTEGER>' 
        set the MAXKMERLENGTH parameter (default 31)

This package builds the sequencespace and colorspace versions of Velvet.

%prep
%setup -n velvet_%{version}

%build
%{__make} %{?categories:'CATEGORIES=%{categories}'} %{?maxkmerlength:'MAXKMERLENGTH=%{maxkmerlength}'}
%{__make} color %{?categories:'CATEGORIES=%{categories}'} %{?maxkmerlength:'MAXKMERLENGTH=%{maxkmerlength}'}

%install
%{__rm} -rf %{buildroot}
%{__install} -m0755 -d %{buildroot}%{_bindir}
%{__install} -m0755 velvetg %{buildroot}%{_bindir}
%{__install} -m0755 velveth %{buildroot}%{_bindir}
%{__install} -m0755 velvetg_de %{buildroot}%{_bindir}
%{__install} -m0755 velveth_de %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS.txt ChangeLog LICENSE.txt README.txt contrib/ *.pdf *.pl
%{_bindir}/*

%changelog
* Fri Oct 08 2010 Steve Huff <shuff@vecna.org> - 1.0.13-1
- Initial package.
