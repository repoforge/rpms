# $Id$
# Authority: yury
# Upstream: Simon Tatham <anakin$pobox,com>

Summary:   Tweak: an efficient hex editor
Name:      tweak
Version:   3.01
Release:   1%{?dist}
License:   MIT
Group:     Applications/Editors
URL:       http://www.chiark.greenend.org.uk/~sgtatham/tweak
Source:    http://www.chiark.greenend.org.uk/~sgtatham/tweak/tweak-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make
BuildRequires: ncurses-devel

%description
Tweak is a hex editor. It allows you to edit a file at very low
level, letting you see the full and exact binary contents of the
file. It can be useful for modifying binary files such as
executables, editing disk or CD images, debugging programs that
generate binary file formats incorrectly, and many other things.

%prep
%setup -q

%build
%{__make} %{?_smp_mflags} XFLAGS="%{optflags}"

%install
%{__make} %{?_smp_mflags} install PREFIX="%{buildroot}%{_prefix}" MANDIR="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc btree.html LICENCE
%doc %{_mandir}/man1/tweak.1.*
%{_bindir}/tweak

%changelog
* Sun Jan 31 2010 Yury V. Zaytsev <yury@shurup.com> - 3.01-1
- Initial package.
- Thanks to Greg Bailey <gbailey@lxpro.com> for the reference package.
