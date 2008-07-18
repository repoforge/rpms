# $Id: $
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_version 0.1.10.r41

Summary: Command line interface to the FreeDesktop.org trashcan
Name: trash-cli
Version: 0.1.10.0.41
Release: 1
License: GPLv2
Group: Applications/File
URL: http://code.google.com/p/trash-cli/

Source: http://dl.sf.net/bluetrash/trash-cli-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel

%description
trash-cli is a command line interface to the FreeDesktop.org trashcan. It 
implements the FreeDesktop.org trash specification. For each trashed file, 
it will remember the name, original path, date of deletion, and permissions. 
It interoperates with KDE Trash, and is CLI compatible with the rm command.

%prep
%setup -n trash-cli-%{real_version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README
%{_bindir}/empty-trash
%{_bindir}/restore-trash
%{_bindir}/list-trash
%{_bindir}/trash
%{python_sitearch}/libtrash.py*

%changelog
* Fri Jul 18 2008 Dries Verachtert <dries@ulyssis.org> - 0.1.10.0.41-1
- Initial package.
