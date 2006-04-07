# $Id$
# Authority: dries
# Upstream: bug-unrtf$gnu,org

Summary: Converts from RTF to other formats
Name: unrtf
Version: 0.20.1
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://www.gnu.org/software/unrtf/unrtf.html

Source: http://www.gnu.org/software/unrtf/unrtf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
UnRTF is a command-line program which converts documents in Rich Text (.rtf)
format to HTML, LaTeX, PostScript, and other formats. Converting to HTML, it
supports font attributes, tables, embedded images (stored to separate
files), paragraph alignment, and more.

%prep
%setup

%{__perl} -pi.orig -e 's|/usr/local/bin|%{buildroot}%{_bindir}|g;' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO
%{_bindir}/unrtf

%changelog
* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.20.1-1
- Updated to release 0.20.1.

* Wed Jan 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.19.3
- Initial package.
