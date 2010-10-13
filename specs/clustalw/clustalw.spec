# $Id$
# Authority: shuff
# Upstream: T.J. Gibson <gibson$embl-heidelberg,de>

Summary: Generate multiple sequence alignment of DNA or protein
Name: clustalw
Version: 1.83
Release: 1%{?dist}
License: Freeware
Group: Applications/Engineering
URL: http://www.ebi.ac.uk/Tools/clustalw/

Source: ftp://ftp.ebi.ac.uk/pub/software/unix/clustalw/clustalw%{version}.UNIX.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
ClustalW is a general purpose multiple sequence alignment program for DNA or
proteins. It produces biologically meaningful multiple sequence alignments of
divergent sequences. It calculates the best match for the selected sequences,
and lines them up so that the identities, similarities and differences can be
seen. Evolutionary relationships can be seen via viewing Cladograms or
Phylograms. 

%prep
%setup -n %{name}%{version}

# online help file goes in %{__datadir}
%{__perl} -pi -e 's|clustalw_help|%{_datadir}/clustalw/clustalw_help|;' clustalw.c

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 clustalw %{buildroot}%{_bindir}

# put online help in %{__datadir}
%{__install} -d -m0755 %{buildroot}%{_datadir}/clustalw
%{__install} -m0644 clustalw_help %{buildroot}%{_datadir}/clustalw

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc clustalw.doc clustalw.ms README 
%doc gon90.bla globin.pep matrixseries.gon 
%{_bindir}/*
%{_datadir}/clustalw/

%changelog
* Wed Oct 13 2010 Steve Huff <shuff@vecna.org> - 1.83-1
- Initial package.
