%define		git_hash e1f8f25
%define		pkg	proto-list
Summary:	A list of objects bound by prototype chain
Name:		nodejs-%{pkg}
Version:	1.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/proto-list
# download from https://github.com/isaacs/%{pkg}/tarball/%%{version}
Source0:	isaacs-%{pkg}-%{version}-0-g%{git_hash}.tar.gz
# Source0-md5:	e69215f7828f63085ae8ab6a82cd9051
#BuildRequires:  nodejs-tap
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A list of objects bound by prototype chain. Used for the Node.js
package manager (npm) configuration.

%prep
%setup -qc
mv isaacs-%{pkg}-*/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}
cp -p %{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}

# We currently don't run tests because I'd have to file another ten or
# so review reuqests for the node.js TAP testing framework and methinks there
# are enough of those for now.  ;-)
##%%check
##%%nodejs %{pkg}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{nodejs_libdir}/%{pkg}.js
